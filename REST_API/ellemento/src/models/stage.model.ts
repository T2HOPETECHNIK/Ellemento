import {Entity, model, property, belongsTo, hasMany} from '@loopback/repository';
import {Tray} from './tray.model';
import {StateWorkflow} from './state-workflow.model';

@model({settings: {strict: false}})
export class Stage extends Entity {
  @property({
    type: 'string',
  })
  stage_name?: string;
  @property({
    type: 'string',
  })
  description?: string;

  @property({
    type: 'number',
  })
  trayTypeId?: number;

  @belongsTo(() => Tray, {name: 'stage_id_tray'})
  stage_id: number;

  @hasMany(() => StateWorkflow)
  stateWorkflows: StateWorkflow[];
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Stage>) {
    super(data);
  }
}

export interface StageRelations {
  // describe navigational properties here
}

export type StageWithRelations = Stage & StageRelations;
